from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sport_event_summary_locale import GetSportEventSummaryLocale
from ...types import Response


def _get_kwargs(
    locale: GetSportEventSummaryLocale,
    urn_sport_event: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/sport_events/{urn_sport_event}/summary",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetSportEventSummaryLocale,
    urn_sport_event: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """show summary for one sport event

     Show a summary for one sport event, including results.

    Args:
        locale (GetSportEventSummaryLocale):
        urn_sport_event (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
        urn_sport_event=urn_sport_event,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    locale: GetSportEventSummaryLocale,
    urn_sport_event: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """show summary for one sport event

     Show a summary for one sport event, including results.

    Args:
        locale (GetSportEventSummaryLocale):
        urn_sport_event (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
        urn_sport_event=urn_sport_event,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
